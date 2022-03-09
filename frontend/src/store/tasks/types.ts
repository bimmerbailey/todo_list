export interface Task {
    id: number;
    description: string;
}

export interface TaskState {
    tasks?: Task;
    error: boolean;
}
