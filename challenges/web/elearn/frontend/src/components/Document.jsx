import React, { useEffect, useState } from 'react'
import Modal from './Modal'
import axios from 'axios'

const Document = props => {
    const { access_token, id, code, lesson_name, name } = props

    const [document, setDocument] = useState({});

    useEffect(() => {
        axios.get(`/api/modules/${code}/lessons/${lesson_name}/documents/${name}`,
            { headers: { Authorization: `JWT ${access_token}` } })
        .then(resp => setDocument(resp.data))
        .catch(console.error)
    }, [setDocument]);

    return (
        <React.Fragment>
            <td>{id}</td>
            <td>{name}</td>
            <td><a href={"#modal-dialog" + id} className="btn btn-primary m-r-5 m-b-5" data-toggle="modal">Download</a></td>
            <td><Modal id={id} title={name} body={document.content} /></td>
        </React.Fragment>
    )
}

export default Document