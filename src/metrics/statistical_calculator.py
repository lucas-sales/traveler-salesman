from src.utils.data_helper import get_results_dataframes
import pandas as pd
df_p, df_m, df_g = get_results_dataframes()


def get_means(df):
    # Definir as colunas agrupadas por métrica
    time_columns = ['Time spent', 'Time spent.1', 'Time spent.2']
    memory_columns = ['Memory used', 'Memory used.1', 'Memory used.2']
    distance_columns = ['Total distance', 'Total distance.1', 'Total distance.2']

    # Calcular a média de 'Time spent', 'Memory used' e 'Total distance' para cada linha usando loc para evitar o warning
    df.loc[:, 'mean_time_spent'] = df[time_columns].mean(axis=1)
    df.loc[:, 'mean_memory_used'] = df[memory_columns].mean(axis=1)
    df.loc[:, 'mean_total_distance'] = df[distance_columns].mean(axis=1)

    # Agrupar os dados por 'File name' e 'algorithm' e calcular as médias
    result = df.groupby(['File name', 'algorithm']).agg(
        mean_time_spent=('mean_time_spent', 'mean'),
        mean_memory_used=('mean_memory_used', 'mean'),
        mean_total_distance=('mean_total_distance', 'mean')
    ).reset_index()

    # Exibir o resultado final
    return result


# medias para cada dataframe
df_p_means = get_means(df_p)
df_m_means = get_means(df_m)
df_g_means = get_means(df_g)
df_final = pd.concat([df_p_means, df_m_means, df_g_means])
df_final['mean_time_spent'] = df_final['mean_time_spent'].round(2)
df_final['mean_memory_used'] = df_final['mean_memory_used'].round(2)
df_final['mean_total_distance'] = df_final['mean_total_distance'].round(2)

df_final.to_csv('/Users/lucassales/Dev/TCC/traveler-salesman/tables/Resultados_medias_finais.csv', index=False)
print(df_final)
