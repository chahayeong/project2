import React from 'react'
import { Schedule as todo } from '../todos'

const Todos = ({children}) => {
    <>
    <h1>Todos</h1>
    <todo />
    {children}
    </>

}

export default Todos