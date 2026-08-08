import React, { useState } from 'react'

function App() {

const [result, setResult] = useState('')

async function testAPI() {

setResult('Testing backend...')

try {

const response = await fetch('/api')

const data = await response.text()

setResult(data)

} catch (error) {

setResult('Backend request failed: ' + error.message)

}

}

return React.createElement(

'main',

null,

React.createElement('h1', null, 'Deploystack Frontend'),

React.createElement('p', null, 'Frontend is running with React + Vite 🚀'),

React.createElement('button', { onClick: testAPI }, 'Test Backend'),

React.createElement('pre', null, result)

)

}

export default App
