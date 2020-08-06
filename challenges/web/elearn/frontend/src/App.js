import React, { Component, useState } from 'react'
import Login from './components/Login'
import Home from './components/Home'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'
import '../public/assets/plugins/jquery-ui-1.10.4/themes/base/minified/jquery-ui.min.css'
import '../public/assets/plugins/bootstrap-3.1.1/css/bootstrap.min.css'
import '../public/assets/plugins/font-awesome-4.1.0/css/font-awesome.min.css'
import '../public/assets/css/animate.min.css'
import '../public/assets/css/style.css'
import '../public/assets/css/style-responsive.css'
import '../public/assets/plugins/gritter/css/jquery.gritter.css'

class App extends Component {
  constructor() {
    super()
    this.state = {
      access_token: null,
      password: '',
    }

    this.setAccessToken = this.setAccessToken.bind(this)
    this.setPassword = this.setPassword.bind(this)
  }

  componentDidMount() {
    const charset = document.createElement('meta')
    charset.charset = 'utf-8'
    document.head.appendChild(charset)

    const viewport = document.createElement('meta')
    viewport.content = 'width=device-width, initial-scale=1.0'
    viewport.name = 'viewport'
    document.head.appendChild(viewport)

    const script = document.createElement('script')
    script.innerHTML = `
      function loadScript(url) {
        return new Promise((resolve, reject) => {
          var script = document.createElement("script")
          script.onload = resolve
          script.onerror = reject
          script.src = url
          document.body.appendChild(script)
        })
      }

      function loadjQuery() {
        if (window.jQuery) {
          // already loaded and ready to go
          return Promise.resolve()
        } else {
          return loadScript("assets/plugins/jquery-1.8.2/jquery-1.8.2.min.js")
        }
      }

      loadjQuery()
        .then(() => loadScript("assets/plugins/jquery-ui-1.10.4/ui/minified/jquery-ui.min.js"))
        .then(() => loadScript("assets/plugins/bootstrap-3.1.1/js/bootstrap.min.js"))
        .then(() => loadScript("assets/plugins/slimscroll/jquery.slimscroll.min.js"))
        .then(() => loadScript("assets/plugins/gritter/js/jquery.gritter.js"))
        .then(() => loadScript("assets/js/apps.min.js"))
        .then(() => {
          const appScript = document.createElement("script")
          appScript.innerHTML = '$(document).ready(() => { App.init() })'
          appScript.defer = true
          document.body.appendChild(appScript)
        })
    `
    script.defer = true
    document.body.appendChild(script)
  }

  setAccessToken(token) {
    this.setState({ access_token: token })
  }

  setPassword(password) {
    this.setState({ password: password })
  }

  render() {
    const { access_token } = this.state
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/login" exact component={() => <Login access_token={access_token} setAccessToken={this.setAccessToken} setPassword={this.setPassword} />} />
          <Route path="/home" component={() => <Home access_token={access_token} password={this.state.password} setAccessToken={this.setAccessToken} />} />
          <Route render={() => <Redirect to="/login" />} />
        </Switch>
      </BrowserRouter>
    )
  }
}

export default App
