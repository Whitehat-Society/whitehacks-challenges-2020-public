import React from 'react';
import { Link } from 'react-router-dom'

const Sidebar = props => {
    const { user, modules } = props

    function viewGrades(e) {
        e.preventDefault()
        const url = `/govtech`
        window.open(url, '_blank')
    }

    return (
        <div id="sidebar" className="sidebar">
            <div data-scrollbar="true" data-height="100%">
                <ul className="nav">
                    <li className="nav-profile">
                        <div className="image">
                            <a href="#"><img src={'/assets/img/user-11.jpg'} alt="" /></a>
                        </div>
                        <div className="info">
                            {user.name}
                            <small>Year 2 Undergraduate</small>
                        </div>
                    </li>
                </ul>

                <ul className="nav">
                    <li className="nav-header">Courses</li>
                    <li className="active">
                        <Link to="/"><i className="fa fa-laptop"></i> <span>Overview</span></Link>
                    </li>
                    {modules.map(module =>
                        <li key={module.code} className="has-sub">
                            <a href="#">
                                <i className="fa fa-suitcase"></i>
                                <span>{module.code}</span>
                            </a>
                        </li>
                    )}

                    {
                        user.id === 3 &&
                        <li className="has-sub">
                            <a href="#" onMouseUp={viewGrades}>
                                <i className="fa fa-cogs"></i>
                                <span>View Past Transcripts</span>
                            </a>
                        </li>
                    }

                    <li className="has-sub" style={{display: 'none'}}>
                        <a href={`/cert/verify`}>
                            <i className="fa fa-cogs"></i>
                            <span>Verify Transcript</span>
                        </a>
                    </li>

                    <li><a href="#" className="sidebar-minify-btn" data-click="sidebar-minify"><i className="fa fa-angle-double-left"></i></a></li>
                </ul>
            </div>
        </div>
    )
}

export default Sidebar