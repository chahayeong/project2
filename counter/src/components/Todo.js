import React, { useState } from 'react'


const Todo = () => {
    const [item, setitem] = useState('')


    return( <>
    <h1> 할일 목록 </h1>
    <h1> {item} </h1>
    <input onChange = { e => setitem(e.target.value)}/><br/>
    <button onClick = { () => { setitem('')}}> 초기화</button>
    </>)
}

export default Todo