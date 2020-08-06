import React, { useEffect, useState } from 'react';
import { Redirect } from 'react-router-dom'
import axios from 'axios'
import Module from './Module'
import Header from './Header'
import Sidebar from './Sidebar'

const Home = props => {
    const { access_token, password, setAccessToken } = props
    if (access_token === undefined || access_token === null) {
        return <Redirect to="/" />
    }
    document.title = 'WhiteHacks Elearn | Home'

    const [user, setUser] = useState({});
    const [modules, setModules] = useState([])
    const auth_header = { headers: { Authorization: `JWT ${access_token}` } }
    useEffect(() => {
        axios.all([axios.get(`/identity`, auth_header),
                   axios.get(`/api/modules`, auth_header)])
            .then(axios.spread((userResp, modulesResp) => {
                setUser(userResp.data)
                setModules(modulesResp.data)
            }))
        .catch(console.error)
    }, [setUser, setModules]);

    return (
        <div id="page-container">
            <Header user={user} modules={modules} access_token={access_token} setAccessToken={setAccessToken} setModules={setModules} />

            <Sidebar user={user} modules={modules} />

            <div id="content" className="content">
                <ol className="breadcrumb pull-right">
                    <li><a href="#">Home</a></li>
                    <li className="active">Overview</li>
                </ol>

                <h1 className="page-header">Overview</h1>
                {modules.map(module => <Module key={module.code} code={module.code} name={module.name} access_token={access_token} />)}
            </div>

            <a href="#" className="btn btn-icon btn-circle btn-success btn-scroll-to-top fade" data-click="scroll-top"><i className="fa fa-angle-up"></i></a>
        </div>
        )
}

export default Home;