#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Streamlit example

"""
import pandas as pd
import copy
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import sklearn.cluster as cluster
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# display title
st.title("🪄 The Muggle Sorting Hat")

# display text
st.subheader("Helping teachers form diverse classes.")

with st.expander("About this app", expanded=False):

    st.write("""Use this app to form diverse classes while making sure that friends stay together.
                 The app first forms groups of friends and then organises them into classes.""")
    st.write("Upload a .csv file with the following columns:")
    st.write("- id (id for every kid)")
    st.write("- previous_class_int (number for kids' previous class)")
    st.write("- color_int (number according to result of psychological test)")
    st.write("- gender_int (number for kids' gender)")
    st.write("- reading_int (number for level of reading skill)")
    st.write("- hobby_int (number for hobby)")
    st.write("- language_int (number for primary language spoken at home)")
    st.write("- introverted_int (number for introverted yes/no)")
    st.write("- siblings (number of siblings)")
    st.write("- friend1 (id of first friend the kid wants to be matched with)")
    st.write("- friend2 (id of second friend the kid wants to be matched with)")

# upload file/use with sample file
csv_uploaded = st.file_uploader("Upload student data")

if csv_uploaded is not None:
    df_uploaded = pd.read_csv(csv_uploaded, index_col=[0])
    st.write(df_uploaded)
else:
        st.info(
            f"""
                Upload a .csv file first. Sample to try: [new_df_friends_small.csv](https://github.com/lbeiermann/sorting_app/blob/main/new_df_friends_small.csv)
                """
        )

# input: number of groups
choice = st.slider("Number of classes", 2, 10)

# get groups of students
def extract_comm(res_number):
    orig_df = df_uploaded
    G_symmetric = nx.Graph()
    for index, row in orig_df.iterrows():
        G_symmetric.add_edge(row["id"], row["friend1"])
        G_symmetric.add_edge(row["id"], row["friend2"])
    c = list(greedy_modularity_communities(G_symmetric, resolution = res_number))
    return c

# turn groups of students into one row in dataframe
def merge_students(res):
    df = df_uploaded
    list_sets = extract_comm(res) # resolution set here
    list_df = []
    for set_students in list_sets:
        mask = df["id"].isin(set_students)
        df_set = df.loc[mask]
        temp_df = pd.DataFrame({"id": [set_students],
                                "number_students": [len(set_students)],
                                "gender_int": [round(df_set["gender_int"].mean(), 1)],
                                "color_int": [round(df_set["color_int"].mean(), 1)],
                                "reading_int": [round(df_set["reading_int"].mean(), 1)],
                                "hobby_int": [round(df_set["hobby_int"].mean(), 1)],
                                "language_int": [round(df_set["language_int"].mean(), 1)],
                                "introverted_int": [round(df_set["introverted_int"].mean(), 1)],
                                "siblings": [round(df_set["siblings"].mean(), 1)],
                                "previous_class_int": [round(df_set["previous_class_int"].mean(), 1)]})
        list_df.append(temp_df)
    merged_communities = pd.concat(list_df, ignore_index=True)
    return merged_communities

# make sklearn pipeline and cluster students
def cluster(df):
    scaler = StandardScaler()
    k = 4
    kmeans = KMeans(n_clusters=k)
    pipeline = make_pipeline(scaler,kmeans)
    pipeline.fit(df[["gender_int", "color_int", "reading_int", "hobby_int", "language_int",
                                 "introverted_int", "siblings", "previous_class_int"]])
    labels = pipeline.predict(df[["gender_int", "color_int", "reading_int", "hobby_int", "language_int",
                                              "introverted_int", "siblings", "previous_class_int"]])
    df["clusters"] = kmeans.labels_
    return df

# make one dataframe for each cluster and add to list
def list_clustered_dataframes(df):
    dataframes_list = []
    for i in df.clusters.unique():
        temporary_df = df[df["clusters"] == i].reset_index(drop=True)
        dataframes_list.append(temporary_df)
        list_sorted = sorted(dataframes_list, key=len, reverse=True)
    return list_sorted

# turn clustered ids into two-dimensional list
def convert_ids(lst):
    ids_clustered = []
    for df in lst:
        ids_clustered.append(df["id"].tolist())
    return ids_clustered

# form classes
def form_classes(lst_ids_clustered, number_classes):
    ids_clustered_new = copy.deepcopy(lst_ids_clustered)
    length = len(df_uploaded)
    max_size = length // number_classes
    ids_classes = []
    for number in range(number_classes):
        ids_classes.append([]) # append an empty list for every class to overall list
    for every_class in ids_classes:
        size = 0
        while size < max_size:
            for lst in ids_clustered_new: # go through the clusters within list of IDs/groups of students
                if len(lst[0]) <= max_size - size: # take group of students from cluster if not too big
                    every_class.append(lst[0]) # add group to class
                    size += len(lst[0]) # change remaining class size
                    del lst[0] # delete group of students from cluster
                    if lst == []:
                        ids_clustered_new.remove(lst) # delete cluster if empty
                else:
                    size = max_size
    return ids_classes, ids_clustered_new

# convert frozenset1 to 2d list
def convert_set_to_list1(st):
    new_lst = []
    for i in st:
        temp_lst = []
        for e in i:
            for j in e:
                temp_lst.append(j)
        new_lst.append(temp_lst)
    return new_lst

# convert frozenset2 to 2d list
def convert_set_to_list2(st):
    new_lst = []
    for i in st:
        for e in i:
            temp_lst = []
            for j in e:
                temp_lst.append(j)
            new_lst.append(temp_lst)
    return new_lst

# convert frozensets to lists
def convert_frozensets(a, b):
    c = convert_set_to_list1(a)
    d = convert_set_to_list2(b)
    return c,d


# adding remaining students #1
def add_rest1(lst_classes, lst_rest):
    merged_list = []
    list1 = sorted(lst_classes, key=len)
    list2 = sorted(lst_rest, key=len, reverse=True)
    for i in range(max((len(list1), len(list2)))):
        while True:
            try:
                list3 = [list1[i], list2[i]]
            except IndexError:
                if len(list1) > len(list2):
                    list2.append([])
                    list3 = [list1[i], list2[i]]
                elif len(list1) < len(list2):
                    list1.append([])
                    list3 = [list1[i], list2[i]]
                continue
            merged_list.append(list3)
            break
    merged_list_cleaned = []
    for i in merged_list:
        list4 = []
        for e in i:
            for j in e:
                list4.append(j)
        merged_list_cleaned.append(list4)
    return merged_list_cleaned

# adding remaining students #2
def add_rest2(cleaned_lst_classes1, number_classes):
    merged_list = []
    list1 = sorted(cleaned_lst_classes1[:number_classes], key = len)
    list2 = sorted(cleaned_lst_classes1[number_classes:], key = len, reverse = True)
    for i in range(max((len(list1), len(list2)))):
          while True:
            try:
                list3 = [list1[i], list2[i]]
            except IndexError:
                if len(list1) > len(list2):
                    list2.append([])
                    list3 = [list1[i], list2[i]]
                elif len(list1) < len(list2):
                    list1.append([])
                    list3 = [list1[i], list2[i]]
                continue
            merged_list.append(list3)
            break
    merged_list_cleaned = []
    for i in merged_list:
        list4 = []
        for e in i:
            for j in e:
                list4.append(j)
        merged_list_cleaned.append(list4)
    return merged_list_cleaned

# get list of final dfs
def make_final_dfs(first_df, list_final_classes):
    list_dfs = []
    for e in list_final_classes:
        new_df = first_df[first_df["id"].isin(e)]
        list_dfs.append(new_df)
    return list_dfs

# get merged df
def final_df_merged(list_final_dfs, i):
    new_list = []
    x = 0
    for df in list_final_dfs:
        x += 1
        class_df = df.copy()
        class_df["class"] = x
        new_list.append(class_df)
    final_df = pd.concat(new_list)
    final_df.reset_index(drop=True, inplace=True)
    original_df = cluster(merge_students(i))
    exp_original_df = original_df.explode("id")
    final_merged_df = final_df.merge(exp_original_df[["id", "clusters"]], how="left", on="id")
    return final_merged_df

# get wish score
def measure_wishs_granted(df):
    friend1_found = df["friend1"].isin(df["id"]).value_counts(normalize=True).reset_index()
    friend1_found.columns = ["friend1_found", "share"]
    wish_score1 = round(friend1_found.loc[friend1_found["friend1_found"] == True, "share"].values[0], 2)

    friend2_found = df["friend2"].isin(df["id"]).value_counts(normalize=True).reset_index()
    friend2_found.columns = ["friend2_found", "share"]
    wish_score2 = round(friend2_found.loc[friend2_found["friend2_found"] == True, "share"].values[0], 2)

    overall_wish_score = round((wish_score1 + wish_score2) / 2, 2)

    return overall_wish_score

# get diversity score
def measure_diversity(df, nb_clusters):
    # calculate ideal score
    ideal_score = 1 / nb_clusters

    # calculate score for current class
    cluster_distribution = df["clusters"].value_counts(normalize=True).reset_index()
    cluster_distribution.columns = ["cluster", "share"]
    diversity_score = round(cluster_distribution["share"].median(), 2) * nb_clusters  # perfect split will turn to 1.0

    return diversity_score

# overall quality check (wish score, diversity, class size)
def quality_check(final_merged_df):
    size_lst = []
    div_score_lst = []
    wish_score_lst = []
    for current_class in pd.unique(final_merged_df["class"]):
        temp_df = final_merged_df[final_merged_df["class"]==current_class]
        size = len(temp_df)
        size_lst.append(size)
        diversity_score = measure_diversity(temp_df, 4)
        div_score_lst.append(diversity_score)
        wish_score = measure_wishs_granted(temp_df)
        wish_score_lst.append(wish_score)
    size_difference = max(size_lst) - min(size_lst)
    overall_div_score = round(sum(div_score_lst) / len(div_score_lst), 2)
    overall_wish_score = round(sum(wish_score_lst) / len(wish_score_lst), 2)
    final_score = round(((overall_div_score + overall_wish_score)/2) + size_difference, 2)
    return final_score

def main(number_classes):  # number of classes

    final_dfs = []
    final_scores = []

    for i in range(14):  # max resolution

        # network analysis and merging students

        df_merged_students = merge_students(i)

        # clustering

        clustered_df = cluster(df_merged_students)
        list_df_clustered = list_clustered_dataframes(clustered_df)
        ids_clustered = convert_ids(list_df_clustered)

        # class formation

        a, b = form_classes(ids_clustered, number_classes)
        list1, list2 = convert_frozensets(a, b)
        final_classes1 = add_rest1(list1, list2)
        final_classes2 = add_rest2(final_classes1, number_classes)
        list_final_dfs = make_final_dfs(df_uploaded, final_classes2)

        # test quality

        final_df = final_df_merged(list_final_dfs, i)
        final_dfs.append(final_df)
        check = quality_check(final_df)
        final_scores.append(check)

    # choose best result

    minpos = final_scores.index(min(final_scores))
    best_df = final_dfs[minpos]
    return best_df

# button
if st.button("Form classes"):
    with st.spinner("Accio classes!"):
        result = main(choice)
    st.dataframe(result)

    # download

    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(result)

    st.download_button(
        "Download classes",
        csv,
        "classes_sorted.csv",
        "text/csv",
        key='download-csv'
    )