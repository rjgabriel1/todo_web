import streamlit as st
import functions

todos = functions.get_todos()
st.title("Simple Todo")
st.write('Manage your daily tasks')


def add_todo():
    task = st.session_state['new_todo'] + "\n"
    todos.append(task)
    functions.set_todos(todos)
    st.session_state.new_todo = ""


st.text_input(label='Enter todo', placeholder="Enter a todo", on_change=add_todo, key='new_todo',
              label_visibility="hidden")

for index, todo in enumerate(todos):
    is_checked = st.checkbox(todo, key=todo)

    if is_checked:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
