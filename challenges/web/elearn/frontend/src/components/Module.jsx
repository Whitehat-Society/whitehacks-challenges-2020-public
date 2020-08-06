import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Lesson from './Lesson'

const Module = props => {
    const { access_token, code, name, grade } = props
    const [lessons, setLessons] = useState([])

    useEffect(() => {
        axios.get(`/api/modules/${code}/lessons`,
            { headers: { Authorization: `JWT ${access_token}` } })
        .then(resp => setLessons(resp.data))
        .catch(console.error)
    }, [setLessons])

    return (
        <div className="panel panel-inverse">
            <div className="panel-heading">
                <h4 className="panel-title">{code} - {name}</h4>
            </div>
            <div className="panel-body">
                {lessons.map(lesson => <Lesson key={lesson.id} code={code} name={lesson.name} access_token={access_token} />)}
            </div>
        </div>
    )
}

export default Module