# Fichier pour centraliser les fonctions
import pandas as pd

'''
Fonction `patients` recupère les données d'un patient spécifique à partir d'un DataFrame.
'''
def indice_patient(numero_patient,data):
    indices_colonnes = []
    for i in range(len(data.iloc[1,1:])):
        if data.iloc[1,i] == numero_patient:
            indices_colonnes.append(i)
    return(indices_colonnes)

def patients(indice,data):
    indice = str(indice)
    ind_patient = indice_patient(indice,data)
    patient = data.iloc[3:,ind_patient]
    #patient = patient.apply(pd.to_numeric)
    #patient = patient.T.astype('float')  #Enlever le commentaire de cette ligne si on veut Transposer la matrice patient
    return(patient)
#----------------


#Fonction pour faire clustering GMM


from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture

def GMM_clustering(data, n_components=2):

    #Normalisation des données
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    #Réduction de dimenison - PCA
    pca = PCA(2)   #2 dimensions pour la visualisation
    data_pca = pca.fit_transform(data_scaled)

    #GMM clustering
    gmm = GaussianMixture(n_components=n_components, random_state=42)
    gmm.fit(data_pca)
    labels = gmm.predict(data_pca)
    data['Cluster'] = labels # Ajout des labels aux données pour utiliser après
    data['Cluster'] = data['Cluster'].astype(str)
    return data, data_pca, pca #, gmm vu que le modele sert juste à la visualisation nous ne le sauvegardons pas

'''
Fonction pour afficher les clusters, en affichant les points extremes
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualisation_clusters(data, data_pca, pca, patient=0, n_extremes=5):
    labels = data['Cluster'].astype(int)

    plt.figure(figsize=(10, 7))
    plt.scatter(data_pca[:, 0], data_pca[:, 1], c=labels, cmap='viridis', s=30)

    # Calcul de la distance de chaque point à l'origine (0,0)
    distances = np.linalg.norm(data_pca[:, :2], axis=1)
    
    # Sélection des indices des points les plus éloignés
    idx_extremes = np.argsort(distances)[-n_extremes:]

    # Annoter uniquement ces points
    for i in idx_extremes:
        gene_name = data.index[i]
        plt.annotate(gene_name, (data_pca[i, 0], data_pca[i, 1]), fontsize=7, fontweight='bold')

    if patient != 0:
        plt.title("Clustering de gènes pour le patient {}".format(patient))
    else:
        plt.title("Clustering de gènes")

    
    # Récupérer la variance expliquée par les 2 premières composantes
    var_ratio = pca.explained_variance_ratio_
    xlabel = f"PCA 1 ({var_ratio[0]*100:.1f}%)"
    ylabel = f"PCA 2 ({var_ratio[1]*100:.1f}%)"

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    #plt.xlabel("PCA 1")
    #plt.ylabel("PCA 2")
    plt.show()

#----------------








