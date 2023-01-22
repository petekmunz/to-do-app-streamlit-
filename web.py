import streamlit as st
import functions as fn

todos = fn.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.set_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox{index}')
    if checkbox:
        todos.pop(index)
        fn.set_todos(todos)
        del st.session_state[f'checkbox{index}']
        st._rerun()

st.text_input(label="Add new todo", label_visibility='hidden', placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
