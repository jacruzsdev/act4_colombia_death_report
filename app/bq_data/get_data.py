import logging

from google.cloud import bigquery
import pandas as pd


def run_bigquery_query(query: str) -> pd.DataFrame:
    """
    Executes a BigQuery query and returns the results as a Pandas DataFrame.

    Args:
        query: The SQL query to execute.

    Returns:
        A Pandas DataFrame containing the query results.  Returns an empty
        DataFrame if the query fails or returns no results.
    """
    try:
        # Construct a BigQuery client object.
        client = bigquery.Client()

        # Try to run the query.
        query_job = client.query(query)  # Make an API request.

        # Get the results as a Pandas DataFrame.
        df = query_job.to_dataframe()

        # logging.info the first few rows of the DataFrame to confirm.
        logging.info("Query results:")
        logging.info(df.head())

        # logging.info the column names and their data types.
        logging.info("\nDataFrame structure:")
        logging.info(df.info())

        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error


def get_report_1() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    The total distribution of deaths per department in Colombia for the year 2019.
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        municipios.DEPARTAMENTO,
        geo_info.Lat,
        geo_info.Long,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo3_divi_pola` municipios ON muertes.COD_DEPARTAMENTO = municipios.COD_DEPARTAMENTO
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo4_geo_info_dept` geo_info ON geo_info.DEPARTAMENTO = municipios.DEPARTAMENTO
    GROUP BY 1,2,3
    """
    return run_bigquery_query(query)


def get_report_2() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    Total monthly deaths in Colombia, illustrating variations throughout the year.
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        muertes.MES,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    GROUP BY 1
    ORDER BY 1 ASC
    """
    return run_bigquery_query(query)


def get_report_3() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    The five most violent cities in Colombia, considering homicides (codes X95, firearm assault, and unspecified cases).
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        CONCAT(municipios.MUNICIPIO, " - ", municipios.DEPARTAMENTO) as Ciudad,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo3_divi_pola` municipios ON muertes.COD_DEPARTAMENTO = municipios.COD_DEPARTAMENTO
    WHERE muertes.COD_MUERTE LIKE"%%X95%%"
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 5
    """
    return run_bigquery_query(query)


def get_report_4() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    The ten leading causes of death in Colombia, including their respective codes, names, and total number of cases.
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        CONCAT(municipios.MUNICIPIO, " - ", municipios.DEPARTAMENTO) as Ciudad,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo3_divi_pola` municipios ON muertes.COD_DEPARTAMENTO = municipios.COD_DEPARTAMENTO
    GROUP BY 1
    ORDER BY 2 ASC
    LIMIT 10
    """
    return run_bigquery_query(query)


def get_report_5() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    The ten leading causes of death in Colombia, including their respective codes, names, and total number of cases.
    :return: a Dataframe with the result
    """
    query = """
    WITH base_query AS (
    SELECT
        muertes.MANERA_MUERTE,
        muertes.COD_MUERTE,
        cods_muerte.Descripcion_4_caracteres,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo2_cods_muerte` cods_muerte ON muertes.COD_MUERTE = cods_muerte.Cod_CIE_10_4_caracteres
    WHERE muertes.COD_MUERTE LIKE"%%X95%%"
    GROUP BY 1,2,3
    ORDER BY 4 DESC
    LIMIT 10
    )
    SELECT
        *
    FROM base_query
    ORDER BY n_muertes asc
    """
    return run_bigquery_query(query)


def get_report_6() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    Distribution of deaths by five-year age groups (0-4, 5-9, …, 85+ years), to identify age ranges with the highest incidence of mortality.
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        muertes.GRUPO_EDAD1,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    GROUP BY 1
    ORDER BY 1 ASC
    """
    return run_bigquery_query(query)


def get_report_7() -> pd.DataFrame:
    """
    Get the query result to get this data req:
    Comparison of the total number of deaths by sex in each department, to analyze significant differences between genders.
    :return: a Dataframe with the result
    """
    query = """
    SELECT
        municipios.DEPARTAMENTO,
        muertes.SEXO,
        count(muertes.COD_MUERTE) n_muertes
    FROM `trusty-equinox-459916-c5.Act3_data.anexo1_no_fetal` muertes
    INNER JOIN `trusty-equinox-459916-c5.Act3_data.anexo3_divi_pola` municipios ON muertes.COD_DEPARTAMENTO = municipios.COD_DEPARTAMENTO
    GROUP BY 1,2
    ORDER BY 1 ASC
    """
    return run_bigquery_query(query)
