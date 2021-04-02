import { Box, Container, Typography } from "@material-ui/core";
import { useSession } from "next-auth/client";
import Head from "next/head";
import { useRouter } from "next/router";
import React from "react";
import Layout from "../../components/layout";

const Redirect: React.FunctionComponent = () => {
  const router = useRouter();
  const [_session, loading] = useSession();
  const path = router.query.path ?? "/";
  const baseUrl = typeof window !== "undefined" ? window.location.origin : "";

  return (
    <>
      {!loading && (
        <Head>
          <meta httpEquiv="refresh" content={`1; URL=${baseUrl}${path}`} />
        </Head>
      )}
      <Layout title={"Redirect"} canonicalUrl="/redirect">
        <Container>
          <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            m={5}
            p={5}
            flexDirection="column"
          >
            {!loading && <Typography className="text-center">Redirecting...</Typography>}
          </Box>
        </Container>
      </Layout>
    </>
  );
};

export default Redirect;
