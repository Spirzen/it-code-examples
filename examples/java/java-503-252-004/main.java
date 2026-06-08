package com.example.bean;

import com.example.model.Task;
import jakarta.enterprise.context.SessionScoped;
import jakarta.faces.application.FacesMessage;
import jakarta.faces.context.FacesContext;
import jakarta.inject.Named;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

@Named("todoBean")
@SessionScoped
public class TodoBean implements Serializable {

    private static final long serialVersionUID = 1L;

    private final List<Task> tasks = new ArrayList<>();
    private String newTaskTitle;

    public void addTask() {
        if (newTaskTitle == null || newTaskTitle.isBlank()) {
            FacesContext.getCurrentInstance().addMessage(null,
                    new FacesMessage(FacesMessage.SEVERITY_WARN,
                            "Введите название задачи", null));
            return;
        }

        tasks.add(new Task(newTaskTitle.trim()));
        newTaskTitle = null;
    }

    public void removeTask(Task task) {
        tasks.remove(task);
    }

    public List<Task> getTasks() {
        return tasks;
    }

    public int getCompletedCount() {
        return (int) tasks.stream().filter(Task::isCompleted).count();
    }

    public String getNewTaskTitle() {
        return newTaskTitle;
    }

    public void setNewTaskTitle(String newTaskTitle) {
        this.newTaskTitle = newTaskTitle;
    }
}
