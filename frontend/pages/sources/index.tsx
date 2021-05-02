import axiosWithoutAuth from "@/axiosWithoutAuth";
import SourceCard from "@/components/modulecards/SourceCard";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { GetServerSideProps } from "next";
import Link from "next/link";
import { FC } from "react";
import Layout from "../../components/Layout";
import Pagination from "../../components/Pagination";

interface SourcesProps {
  sourcesData: any;
}

const Sources: FC<SourcesProps> = ({ sourcesData }: SourcesProps) => {
  const sources = sourcesData["results"] || [];
  const sourceCards = sources.map((source) => (
    <Grid item key={source["slug"]} xs={6} sm={4} md={3}>
      <Link href={`/sources/${source["slug"]}`}>
        <a>
          <SourceCard source={source} />
        </a>
      </Link>
    </Grid>
  ));

  return (
    <Layout title={"Sources"}>
      <Container>
        <Pagination count={sourcesData["total_pages"]} />
        <Grid container spacing={2}>
          {sourceCards}
        </Grid>
        <Pagination count={sourcesData["total_pages"]} />
      </Container>
    </Layout>
  );
};

export default Sources;

// https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering
export const getServerSideProps: GetServerSideProps = async (context) => {
  let sourcesData = {};

  await axiosWithoutAuth
    .get("http://django:8000/api/sources/", { params: context.query })
    .then((response) => {
      sourcesData = response.data;
    })
    .catch((error) => {
      // console.error(error);
    });

  return {
    props: {
      sourcesData,
    },
  };
};