import streamlit as st
from functions import get_todos, write_todos

st.title("My Todo App")
st.subheader("This is my new todo app")
st.write("This app is to improve prodictivity")

todos = get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new To-Do item here...",
              on_change=add_todo, key='new_todo')
