package com.example.todolist

import android.graphics.Paint.STRIKE_THRU_TEXT_FLAG
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_todo.view.*


// Contains main logic of app

// Class takes kotlin list of items to populate list with

// Inside brackets is the constructor

class TodoAdapter(
    // Can only be accessed inside this class

    // The type is the Todo class
    private val todos: MutableList<Todo>
) : RecyclerView.Adapter<TodoAdapter.TodoViewHolder>() {
    // Holds layout of specific item - achieves recycler view behaviour
    // Imported above when you press enter
    class TodoViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TodoViewHolder {
        // Creates this Todo view holder - need to defeine how a specific item in list looks lik

        return TodoViewHolder(
            // Inflator converts XML style ot Kotlin class
            // COntex = state of application
            // Parent = viewGrouo layout - gets reference to context
            LayoutInflater.from(parent.context).inflate(
                // Resource id
                R.layout.item_todo,
                parent,
                false
            )

        )
    }

    fun addTodo(todo: Todo) {
        todos.add(todo)

        notifyItemInserted(todos.size-1)
    }

    fun deleteDoneTodos() {
        todos.removeAll{todo ->
            todo.isChecked
        }

        notifyDataSetChanged()
    }

    // Strikethrough text when button clicked
    private fun toggleStrikeThrough(tvTodoTitle: TextView, isChecked: Boolean){
        if(isChecked) {
            tvTodoTitle.paintFlags = tvTodoTitle.paintFlags or STRIKE_THRU_TEXT_FLAG
        } else {
            tvTodoTitle.paintFlags = tvTodoTitle.paintFlags and STRIKE_THRU_TEXT_FLAG.inv() //inverted + binary and
        }
    }

    override fun onBindViewHolder(holder: TodoViewHolder, position: Int) {
        // Bind data from todos list to views of our list - called when a new list item in list is visible
        // Holder = gets access to text view and check box  - position = gets its position

        // Pos is the current todo item
        val curTodo = todos[position]
        // Apply = Kotlin feature so don't have to prepend holder.itemView every time
        holder.itemView.apply {
            // Set text of text view to the title of this current todo item
            tvTodoTitle.text = curTodo.title
            cbDone.isChecked = curTodo.isChecked
            toggleStrikeThrough(tvTodoTitle, curTodo.isChecked)
            // if u clicked on checkbox, the variable is true
            // _ means u dont need that arg
            cbDone.setOnCheckedChangeListener {_, isChecked ->
                toggleStrikeThrough(tvTodoTitle, isChecked)
                curTodo.isChecked = !curTodo.isChecked
            }

        }

    }

    override fun getItemCount(): Int {
        // Returns amount of items in list
        return todos.size
    }
}