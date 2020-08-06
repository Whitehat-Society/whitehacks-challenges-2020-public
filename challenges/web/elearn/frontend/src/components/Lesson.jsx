import React, { useEffect, useState } from 'react'
import Document from './Document'
import axios from 'axios'

const Lesson = props => {
  const { access_token, code, name } = props

  const [documents, setDocuments] = useState([])

  useEffect(() => {
    axios.get(`/api/modules/${code}/lessons/${name}/documents`,
      { headers: { Authorization: `JWT ${access_token}` } })
    .then(resp => setDocuments(resp.data))
    .catch(console.error)
  }, [setDocuments])

  return (
    <table className="table table-striped">
        <thead>
            <tr><th colSpan="2"><h3>{name}</h3></th></tr>
        </thead>
        <tbody>
            {documents.map(document => <tr key={document.id}><Document access_token={access_token} id={document.id} code={code} lesson_name={name} name={document.name} /></tr>)}
        </tbody>
    </table>
  )
}

export default Lesson