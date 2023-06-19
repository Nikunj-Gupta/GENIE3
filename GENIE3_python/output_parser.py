import pandas as pd 

SAVE = True  


def map_gene_symbol(name_id): 
    name = GSE65391_top_table[GSE65391_top_table["ID"]==name_id]["Gene.symbol"].values[0] 
    if type(name)==float: name = "NA" 
    return name 


Ranked_list_TF_gene_best_model = pd.read_csv("ranking_test.txt", delimiter="\t", header=None) 
Ranked_list_TF_gene_best_model = Ranked_list_TF_gene_best_model.rename(columns={0: "TF", 1: "Target", 2: "Importance"}) 
_parsed_Ranked_list_TF_gene_best_model = pd.DataFrame(columns=Ranked_list_TF_gene_best_model.columns) 

GSE65391_top_table = pd.read_csv("GEO_dataset/GSE65391/GSE65391.top.table.tsv", delimiter="\t") 

Ranked_list_TF_gene_best_model["TF.Gene.Symbol"] = [map_gene_symbol(tf) for tf in Ranked_list_TF_gene_best_model["TF"].to_numpy().tolist()] 
Ranked_list_TF_gene_best_model["Target.Gene.Symbol"] = [map_gene_symbol(target) for target in Ranked_list_TF_gene_best_model["Target"].to_numpy().tolist()] 


_parsed_Ranked_list_TF_gene_best_model = Ranked_list_TF_gene_best_model[["TF.Gene.Symbol", "Target.Gene.Symbol", "Importance"]] 

if SAVE: _parsed_Ranked_list_TF_gene_best_model.to_csv("_parsed_ranking_test.csv", index=False) 

