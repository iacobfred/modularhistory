import { AxiosResponse } from "axios";
import { NextApiHandler, NextApiRequest, NextApiResponse } from "next";
import NextAuth, { CallbacksOptions, NextAuthOptions, PagesOptions, Session as NextAuthSession, User as NextAuthUser } from "next-auth";
import { JWT as NextAuthJWT } from "next-auth/jwt";
import Providers from "next-auth/providers";
import { WithAdditionalParams } from "next-auth/_utils";
import axios from '../../../axios';

const makeDjangoApiUrl = (endpoint) => {
  return `http://django:8000/api${endpoint}`;
};

interface JWT extends NextAuthJWT {
  accessToken: string
  cookies: Array<string>
  error: string
}

interface User extends NextAuthUser {
  accessToken: string
  refreshToken: string
  cookies: Array<string>
  error: string
}
interface Session extends NextAuthSession {
  cookies: Array<string>
}

// https://next-auth.js.org/configuration/providers
const providers = [
  // TODO: https://next-auth.js.org/providers/discord
  // TODO: https://modularhistory.atlassian.net/browse/MH-136
  // Providers.Discord({
  //   clientId: process.env.SOCIAL_AUTH_DISCORD_CLIENT_ID,
  //   clientSecret: process.env.SOCIAL_AUTH_DISCORD_SECRET
  // }),
  // // TODO: https://next-auth.js.org/providers/facebook
  // Providers.Facebook({
  //   clientId: process.env.SOCIAL_AUTH_FACEBOOK_KEY,
  //   clientSecret: process.env.SOCIAL_AUTH_FACEBOOK_SECRET,
  // }),
  // // TODO: https://next-auth.js.org/providers/google
  // Providers.Google({
  //   clientId: process.env.SOCIAL_AUTH_GOOGLE_KEY,
  //   clientSecret: process.env.SOCIAL_AUTH_GOOGLE_SECRET,
  // }),
  // // TODO: https://next-auth.js.org/providers/twitter
  // Providers.Twitter({
  //   clientId: process.env.SOCIAL_AUTH_TWITTER_KEY,
  //   clientSecret: process.env.SOCIAL_AUTH_TWITTER_SECRET,
  // }),
  // // TODO: https://next-auth.js.org/providers/github
  // Providers.GitHub({
  //   clientId: process.env.SOCIAL_AUTH_GITHUB_KEY,
  //   clientSecret: process.env.SOCIAL_AUTH_GITHUB_SECRET,
  // }),
  // TODO: https://next-auth.js.org/providers/credentials
  Providers.Credentials({
    id: "credentials",
    // The name to display on the sign-in form (i.e., 'Sign in with ...')
    name: "Credentials",
    // The fields expected to be submitted in the sign-in form
    credentials: {
      username: { label: "Username", type: "text", placeholder: "" },
      password: { label: "Password", type: "password" },
    },
    async authorize(credentials) {
      const url = makeDjangoApiUrl("/users/auth/login/");
      // TODO: Use state? See https://github.com/iMerica/dj-rest-auth/blob/master/demo/react-spa/src/App.js.
      let user;
      await axios
      .post(url, {
        username: credentials.username,
        password: credentials.password,
      })
      .then(function (response: AxiosResponse) {
        user = response.data["user"];
        if (!user) {
          throw new Error(`${response}`);
        }
        /*
          Attach necessary values to the user object.
          Subsequently, the JWT callback reads these values from the user object 
          and attaches them to the token object it returns.
        */
        user.accessToken = response.data.access_token;
        user.refreshToken = response.data.refresh_token;
        user.cookies = response.headers['set-cookie'];
        return Promise.resolve(user);
      })
      .catch(function (error) {
        console.error(`Failed to authenticate due to error:\n${error}`);
        throw new Error(`${error}`);
      });
      return Promise.resolve(user);
    }
  }),
];

// https://next-auth.js.org/tutorials/refresh-token-rotation
async function refreshAccessToken(jwt) {
  /*
    Return a new token with updated `accessToken` and `accessTokenExpiry`. 
    If an error occurs, return the old token with an error property.
    jwt contains name, email, accessToken, cookies, refreshToken, accessTokenExpiry, iat, exp.
  */
  await axios
  .post(makeDjangoApiUrl("/users/auth/token/refresh/"), {
    refresh: jwt.refreshToken
  })
  .then(function (response: AxiosResponse) {
    /*
      If the refresh token was invalid, the API responds:
      {
        "detail": "Token is invalid or expired", 
        "code": "token_not_valid"
      }

      If the refresh token was valid, the API responds:
      {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2NzAzODQzLCJqdGkiOiI0NTY0Y2I3MDI2ZDY0MGNiODJmMWQ3MDlhNDc4ZjAwYiIsInVzZXJfaWQiOjQzfQ.bUaqKjtFn-WvCU0uWngly0HZdKFEXgsq3J_XsjG66ic",
        "access_token_expiration": "2021-03-25T20:24:03.605165Z"
      }
    */
    console.log('Refreshed auth token successfully.');
    if (response.data.access && response.data.access_token_expiration) {
      jwt = {
        ...jwt,
        // Fall back to old refresh token if necessary.
        refreshToken: response.data.refresh_token ?? jwt.refreshToken,
        accessToken: response.data.access,
        accessTokenExpiry: Date.now() + Date.parse(response.data.access_token_expiration),
        cookies: response.headers['set-cookie']
      };
    } else {
      throw new Error(`Failed to parse response data: ${response.data}`);
    }
  })
  .catch(function (error) {
    console.error(`Failed to refresh auth token due to error:\n${error}`);
    return {
      ...jwt,
      error: "RefreshAccessTokenError",
    };
  });
  return jwt;
}

// https://next-auth.js.org/configuration/callbacks
const callbacks: CallbacksOptions = {};

callbacks.signIn = async function signIn(user: User, provider, data) {
  let accessToken: string;
  let refreshToken: string;
  let cookies: Array<string>;
  if (provider.id === "credentials") {
    /*
      Coming from the credentials provider, `data` is of this form:
      {
        csrfToken: 'example',
        username: 'example',
        password: 'example'
      }
    */
    accessToken = user.accessToken;
    refreshToken = user.refreshToken;
    cookies = user.cookies;
  } else {
    let socialUser;
    console.log("\nsignIn.data: ", data);
    switch (provider.id) {
      case "discord":  // https://next-auth.js.org/providers/discord
        socialUser = {
          id: data.id,
          login: data.login,
          name: data.name,
          avatar: user.image,
        };
        break;
      case "facebook":  // https://next-auth.js.org/providers/facebook
        socialUser = {
          id: data.id,
          login: data.login,
          name: data.name,
          avatar: user.image,
        };
        break;
      case "github":  // https://next-auth.js.org/providers/github
        // TODO: https://modularhistory.atlassian.net/browse/MH-136
        // https://getstarted.sh/bulletproof-next/add-social-authentication/5
        // const emailRes = await fetch('https://api.github.com/user/emails', {
        //   headers: {
        //     'Authorization': `token ${account.accessToken}`
        //   }
        // })
        // const emails = await emailRes.json()
        // const primaryEmail = emails.find(e => e.primary).email;
        // user.email = primaryEmail;
        socialUser = {
          id: data.id,
          login: data.login,
          name: data.name,
          avatar: user.image,
        };
        break;
      case "google":  // https://next-auth.js.org/providers/google
        socialUser = {
          id: data.id,
          login: data.login,
          name: data.name,
          avatar: user.image,
        };
        break;
      case "twitter":  // https://next-auth.js.org/providers/twitter
        socialUser = {
          id: data.id,
          login: data.login,
          name: data.name,
          avatar: user.image,
        };
        break;
      default:
        return false;
    }
    accessToken = accessToken || null;  // TODO: https://modularhistory.atlassian.net/browse/MH-136: await getTokenFromYourAPIServer(account.provider, socialUser);
    refreshToken = refreshToken || null;  // TODO: https://modularhistory.atlassian.net/browse/MH-136: await getTokenFromYourAPIServer(account.provider, socialUser);
    cookies = cookies || null;
  }
  user.accessToken = accessToken;
  user.refreshToken = refreshToken;
  user.cookies = cookies;
  console.log('');
  return true;
};

// https://next-auth.js.org/configuration/callbacks#jwt-callback
callbacks.jwt = async function jwt(token, user?: User, account?, profile?, isNewUser?: boolean) {
  // The arguments user, account, profile and isNewUser are only passed the first time 
  // this callback is called on a new session, after the user signs in.
  if (user && account) {  // initial sign in
    token.accessToken = user.accessToken || account.accessToken;  // TODO: https://modularhistory.atlassian.net/browse/MH-136
    token.cookies = user.cookies;
    token.refreshToken = user.refreshToken || account.refresh_token;  // TODO: https://modularhistory.atlassian.net/browse/MH-136
  }
  if (token.cookies) {
    let sessionTokenCookie;
    token.cookies.forEach(cookie => {
      if (cookie.startsWith('next-auth.session-token=')) {
        sessionTokenCookie = cookie;
      }
    });
    token.accessTokenExpiry = token.accessTokenExpiry ?? Date.parse(sessionTokenCookie.match(/expires=(.+?);/)[1]);
  }
  if (Date.now() > token.accessTokenExpiry) {
    token = await refreshAccessToken(token);
  }
  return Promise.resolve(token);
};

callbacks.session = async function session(session: Session, userOrToken: User | JWT) {
  const sessionPlus: WithAdditionalParams<Session> = {...session};
  if (userOrToken) {
    if (userOrToken.error) {
      sessionPlus.error = userOrToken.error;
    } else {
      const accessToken = userOrToken.accessToken;
      if (accessToken) {
        sessionPlus.accessToken = accessToken;
        sessionPlus.cookies = userOrToken.cookies;
        let userData;
        await axios
        .get(makeDjangoApiUrl("/users/me/"), {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          }
        })
        .then(function (response: AxiosResponse) {
          userData = response.data;
        })
        .catch(function (error) {
          console.error(error);
        });
        sessionPlus.user = userData;
      }
    }
  }
  return sessionPlus;
};

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');  // $& means the whole matched string
}

callbacks.redirect = async function redirect(url, baseUrl) {
  const preUrl = url;
  const re = new RegExp(`(\\?callbackUrl=${escapeRegExp(baseUrl)}\\/auth\\/signin)+`);
  url = preUrl.replace(re, `?callbackUrl=${baseUrl}/auth/signin`);
  if (url != preUrl) {
    console.log(`Changed redirect URL from ${preUrl} to ${url}`);
  }
  return url;
}

// https://next-auth.js.org/configuration/pages
const pages: PagesOptions = {
  signIn: "/auth/signin",
  signOut: "/auth/signout",
}

const options: NextAuthOptions = {
  // https://next-auth.js.org/configuration/options#callbacks
  callbacks: callbacks,
  // https://next-auth.js.org/configuration/options#jwt
  jwt: {secret: process.env.SECRET_KEY},
  // https://next-auth.js.org/configuration/pages
  pages: pages,
  // https://next-auth.js.org/configuration/options#providers
  providers: providers,
  // https://next-auth.js.org/configuration/options#secret
  secret: process.env.SECRET_KEY,
  // https://next-auth.js.org/configuration/options#session
  session: {jwt: true},
};

const authHandler: NextApiHandler = (req: NextApiRequest, res: NextApiResponse) => {
  return NextAuth(req, res, options);
};

export default authHandler;

// TODO: https://modularhistory.atlassian.net/browse/MH-136
async function getTokenFromDjangoServer(user: User) {
  const url = makeDjangoApiUrl("/token/obtain");
  const response = "";
  // const response = await axios
  //   .post(url, {
  //     username: credentials.username,
  //     password: credentials.password,
  //   })
  //   .then(function (response) {
  //     // handle success
  //     console.log(response);
  //   })
  //   .catch(function (error) {
  //     // handle error
  //     console.error(error);
  //   });
  return response;
}
