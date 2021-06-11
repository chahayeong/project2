import { createStore } from 'redux'
import {default as todoReducer} from './todo.reducer'
export { todoReducer } from './todo.reducer'
export const store = createStore(todoReducer)