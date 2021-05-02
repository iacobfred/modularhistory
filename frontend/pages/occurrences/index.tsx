import axiosWithoutAuth from "@/axiosWithoutAuth";
import OccurrenceCard from "@/components/modulecards/OccurrenceCard";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { GetServerSideProps } from "next";
import Link from "next/link";
import { FC } from "react";
import Layout from "../../components/Layout";
import Pagination from "../../components/Pagination";

interface OccurrencesProps {
  occurrencesData: any;
}

const Occurrences: FC<OccurrencesProps> = ({ occurrencesData }: OccurrencesProps) => {
  const occurrences = occurrencesData["results"] || [];
  const occurrenceCards = occurrences.map((occurrence) => (
    <Grid item key={occurrence["slug"]} xs={6} sm={4} md={3}>
      <Link href={`/occurrences/${occurrence["slug"]}`}>
        <a>
          <OccurrenceCard occurrence={occurrence} />
        </a>
      </Link>
    </Grid>
  ));

  return (
    <Layout title={"Occurrences"}>
      <Container>
        <Pagination count={occurrencesData["total_pages"]} />
        <Grid container spacing={2}>
          {occurrenceCards}
        </Grid>
        <Pagination count={occurrencesData["total_pages"]} />
      </Container>
    </Layout>
  );
};

export default Occurrences;

// https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering
export const getServerSideProps: GetServerSideProps = async (context) => {
  let occurrencesData = {};

  await axiosWithoutAuth
    .get("http://django:8000/api/occurrences/", { params: context.query })
    .then((response) => {
      occurrencesData = response.data;
    })
    .catch((error) => {
      // console.error(error);
    });

  return {
    props: {
      occurrencesData,
    },
  };
};