from Graph import create_dataframe
from Graph import build_graph
from Graph import get_shortest_way
from Graph import get_keywords

data_base_file = 'SciFinder_data.db'
df = create_dataframe(data_base_file, kwords_to_list=True)


id_list = df['pubmed_id']
keywords_list = df['keywords']
Graph = build_graph(id_list, keywords_list, drow=False)

A = '37587511'
C = '37586403'
short_way = get_shortest_way(Graph, A, C, drow=True)

B = '37583417'
matched_words = get_keywords(B, C, df)
print(matched_words)
