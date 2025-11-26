# m1-stage-scanalysis 🔬

This repository contains the code and the accompanying PDF report describing my contribution to a research project conducted between **Université Lumière Lyon 2** and the **Cancer Research Center of Lyon (CRCL)**.  
The goal of this internship project was to analyze **single-cell RNA sequencing (scRNA-seq) data** from patients with skin cancer and identify the most effective methods to visualize and interpret this highly complex, high-dimensional data.

---

## 🔍 Project Context

Single-cell data is characterized by:
- High dimensionality (thousands of genes per cell)
- Strong sparsity due to dropout events
- High variability between cells and patients
- A typical **p >> n** problem (more variables than observations)

These properties make classical analysis difficult and require dimensionality reduction and probabilistic modeling techniques adapted to scRNA-seq.

---

## 🧠 Methods Used

### **scVI (Single-cell Variational Inference)**
One of the most informative and robust methods used in this project was **scVI**, a deep generative model based on **variational autoencoders (VAE)**.  
scVI models gene expression using a probabilistic latent space that captures biological variability while correcting for:
- Batch effects  
- Technical noise  
- Overdispersion  

This allowed us to obtain a **clean and biologically meaningful latent representation** of the data.

### **Dimensionality Reduction**
We used several visualization techniques, including:

- **t-SNE**  
  Provides a non-linear projection of high-dimensional embeddings, particularly effective at preserving local neighborhood structure.  
  Although t-SNE is stochastic and may converge to different minima, the clustering patterns observed in our project remained **consistently stable across multiple runs**,   reinforcing the robustness of the underlying biological structure.

- **UMAP**  
  Another non-linear dimensionality reduction method, known for preserving both **local and global structure** more effectively than t-SNE.  
  UMAP often provides clearer separation between clusters and is computationally efficient, making it a strong candidate for visualizing large single-cell datasets.

- **PCA**  
  A linear projection method and the most stable of the approaches.  
  However, due to the noisy and sparse nature of single-cell data, PCA often requires exploring **a large number of components** to capture biologically meaningful variability.  
  As a result, cluster structure may only become visible in higher-dimensional PCA spaces.

- **Spectral Embedding**  
  Based on graph Laplacian eigenvectors, this method captures the structure of the data by modeling it as a graph.  
  Spectral embedding can reveal **manifold structures** that are not detectable through purely linear methods, making it useful for datasets with complex geometric organization.  
  However, its performance is highly dependent on the choice of kernel and graph construction parameters.


### **Clustering**
Clusters obtained from the scVI latent space showed consistent grouping patterns across patients, suggesting biological structure in the data.

---

## 📈 Results

- Clear and stable cluster structures emerged from the scVI latent space.  
- t-SNE visualizations confirmed the robustness of these clusters, despite the stochastic nature of the method.  
- The project highlighted the benefits of **deep generative models** over traditional PCA-only workflows for single-cell interpretation.

---

## 🧪 Challenges & Skills Developed

This internship presented several technical and conceptual challenges due to the complexity of single-cell data.  
However, overcoming these difficulties allowed me to develop a set of **highly transferable skills**, valuable in a wide range of data science and machine learning projects:

- **Advanced literature review skills**  
  I had to conduct extensive bibliographic research to understand single-cell mechanisms, data preprocessing strategies, and state-of-the-art modeling techniques.  
  This strengthened my ability to quickly learn new domains, evaluate scientific sources, and apply research-driven insights to complex problems.

- **Problem-solving in high-dimensional and noisy environments**  
  Single-cell data is sparse, noisy, and extremely high-dimensional. Working with it improved my capacity to design and adapt methods that remain effective under difficult data conditions.

- **Ability to propose methodological solutions in uncertain or ambiguous situations**  
  Many decisions—model choice, preprocessing strategy, visualization technique—required navigating incomplete information and comparing multiple alternatives.  
  I learned to justify methodological choices, explore different paths, and converge toward robust solutions.

- **Critical thinking and result interpretation**  
  Evaluating clustering stability, detecting artifacts, and interpreting latent representations demanded careful reasoning and a rigorous approach to analysis.

- **Workflow structuring and reproducibility**  
  Designing a full analysis pipeline (preprocessing → modeling → visualization → interpretation) strengthened my ability to structure reproducible experiments and organize code efficiently.

These skills are broadly applicable to fields such as **machine learning, data science, NLP, bioinformatics, computer vision, and MLOps**, where complex data and methodological uncertainty are frequent challenges.

---

## 📄 More Details

The **full methodology, experiments, and results** are detailed in the PDF report (in French) included in this repository.

