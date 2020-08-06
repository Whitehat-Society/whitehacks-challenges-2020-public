import React, { useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Header = props => {
    const { access_token, user, setModules } = props

    const [navbar, setNavbar] = useState("dropdown navbar-user");

    function toggleUserDropdown() {
        const navbarUser = document.getElementsByClassName('navbar-user')[0]
        if (navbarUser.className.endsWith('open')) {
            setNavbar("dropdown navbar-user")
        } else {
            setNavbar("dropdown navbar-user open")
        }
    }

    function onSubmit(e) {
        e.preventDefault()
        const search = document.getElementById('search').value
        const auth_header = { headers: { Authorization: `JWT ${access_token}` } }
        axios.get(`/api/modules/search/${search}`, auth_header)
            .then(resp => setModules(resp.data))
    }

    function onLogout() {
        props.setAccessToken(null)
    }

    return (
        <div id="header" className="header navbar navbar-default navbar-fixed-top">
            <div className="container-fluid">
                <div className="navbar-header">
                    <a href="/" className="navbar-brand"><span className="navbar-logo"></span> WhiteHacks</a>
                    <button type="button" className="navbar-toggle" data-click="sidebar-toggled">
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                    </button>
                </div>

                <ul className="nav navbar-nav navbar-right">
                    <li>
                        <form className="navbar-form full-width" onSubmit={onSubmit}>
                            <div className="form-group">
                                <input id="search" type="text" className="form-control" placeholder="Enter keyword" />
                                <button type="submit" className="btn btn-search"><i className="fa fa-search"></i></button>
                            </div>
                        </form>
                    </li>
                    <li className={navbar}>
                        <a href="#" className="dropdown-toggle" data-toggle="dropdown" onClick={toggleUserDropdown}>
                            <img src={'/assets/img/user-11.jpg'} alt="" />
                            <span className="hidden-xs">{user.name}</span> <b className="caret"></b>
                        </a>
                        <ul className="dropdown-menu animated fadeInLeft">
                            <li className="arrow"></li>
                            <li><Link to="/" onClick={onLogout}>Log Out</Link></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default Header