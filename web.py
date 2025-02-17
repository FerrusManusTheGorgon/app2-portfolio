import streamlit as st
import functions

FILEPATH = "/Users/seanyoung/PycharmProjects/pythonProject/todos.txt"

todos = functions.get_todos(FILEPATH)


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(FILEPATH, todos)
    st.session_state["new_todo"] = ""

def remove_todo(index):
    """Remove a todo item from the list by index and save changes."""
    st.session_state.todos.pop(index)  # Remove the todo from the session state list
    functions.write_todos(FILEPATH, st.session_state.todos)  # Save the updated list to file


# todos = functions.get_todos("/Users/seanyoung/PycharmProjects/pythonProject/todos.txt")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(FILEPATH, todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


st.session_state