import streamlit as st
#app title
st.title('to_do list app')
#installation sassion state for task
if 'task' not in st.session_state:
    st.session_state['task']=[]
#sidebar hadding
st.sidebar.header("manage your task")
#text input
new_task = st.sidebar.text_input("enter new task")

if st.sidebar.button('add task'):
    if new_task.strip():
        st.session_state.task.append({"task": new_task,"completed":False})
        st.success("task added successfully")
        st.session_state.new_task = ""
    else:
            st.warning("task cannot be empty!")
# display task
st.subheader("your to_do list")
if not st.session_state.task:
    st.info("no task added yet start by adding a task from tha sidebar!")
else:
    for index, task in enumerate(st.session_state.task):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.16])

        # mark as completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.task[index]["completed"] = completed

        # UPDATE TASK
        if col2.button("edit", key=f"edit_{index}"):
            new_task = st.text_input("edit task", task["task"])
            if new_task and st.button("save", key=f"save_{index}"):
                st.session_state.task[index]["task"] = new_task
                st.experimental_rerun()

        # delete task
        if col3.button("delete", key=f"delete_{index}"):
            del st.session_state.task[index]
            st.experimental_rerun()

#clear akk task
if st.button("clear all tasks"):
    st.session_state.task = []
    st.success("all tasks cleared successfully")
#footer
st.markdown("---")
st.caption("stay organized and prodective with simple to-do list app")
