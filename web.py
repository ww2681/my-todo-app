import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    get_new_todo = st.session_state["new_todo"] + "\n"
    todos.append(get_new_todo)
    functions.write_todo(todos)


st.title("My Todo App")
st.subheader("By Wenna")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
