README

--- The Muggle Sorting Hat ---
--- A TechLabs Project ---

Our app helps teachers form diverse classes while making sure that friends stay together.

---

Folder overview:

"First ideas": documents produced during initial brainstorms

"Jupyter notebooks": notebooks we used to try out ideas

"Presentations": presentation/pitch files

"Test datasets": datasets of students we made to test our app

"The Muggle Sorting Hat": ideas for final streamlit prototype (incl. psychological test, concept, sample data)

---

The Muggle Sorting Hat first uses network analysis to form groups of friends, then clusters them (kmeans)
based on various criteria (e.g. previous school, primary language spoken at home, ...), then takes groups 
from each cluster and organises them into diverse classes of students.

To run The Muggle Sorting Hat on streamlit, follow this link: https://share.streamlit.io/lbeiermann/the-muggle-sorting-hat/main/streamlit_prototype.py. 
Upload the sample data in the "The Muggle Sorting Hat" folder, eg. "new_df_friends_small.csv", pick a number of classes and run the app.

