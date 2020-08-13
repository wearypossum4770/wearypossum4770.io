import React from 'react'
import './styles/App.css'
import CashFlowContainer from './containers/CashFlowContainer'
import CurrentAssets from './containers/CurrentAssets'
import {lightTheme, darkTheme} from './themes/index.js'
import {ThemeProvider} from './src/context/theme-context.js'

function App({element}) {
    return <ThemeProvider>{element}</ThemeProvider>
}

export default App
