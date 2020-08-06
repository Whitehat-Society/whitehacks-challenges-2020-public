import React from 'react';
import axios from 'axios'
import { Redirect } from 'react-router-dom'

const Root = props => {
    const { access_token } = props
    if (access_token !== undefined && access_token !== null) {
        return <Redirect to="/home" />
    }
    document.title = 'WhiteHacks Elearn | Login Page'

    function onSubmit(e) {
        e.preventDefault()
        const username = document.getElementById('username')
        const password = document.getElementById('password')
        axios.post(`/auth`, {
            username: username.value,
            password: password.value,
        })
        .then(resp => {
            const token = resp.data.access_token
            props.setAccessToken(token)
            props.setPassword(password.value)
            return <Redirect to="/home" />
        })
        .catch(console.error)
    }

    return (
        <React.Fragment>
            <div id="page-container">
                <div className="login bg-black animated fadeInDown">
                    <div className="login-header">
                        <div className="brand">
                            <span className="logo"></span> WhiteHacks Elearn
                        </div>
                    </div>

                    <div className="login-content">
                        <form action="" onSubmit={onSubmit} method="POST" className="margin-bottom-0">
                            <div className="form-group m-b-20">
                                <input id="username" type="text" className="form-control input-lg" placeholder="Username" />
                            </div>
                            <div className="form-group m-b-20">
                                <input id="password" type="password" className="form-control input-lg" placeholder="Password" />
                            </div>
                            <div className="login-buttons">
                                <button type="submit" className="btn btn-success btn-block btn-lg">Sign me in</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </React.Fragment>
        )
}

export default Root