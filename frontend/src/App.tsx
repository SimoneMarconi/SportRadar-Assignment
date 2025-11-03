import { useState } from 'react'
import './css/App.css'
import { PageState } from './types/sportEnums'
import MatchesCalendar from './components/MatchesCalendar'
import LeaderBoard from './components/LeaderBoard'
import TopBar from './components/TopBar'
import { Toaster } from 'sonner'
import {AppProvider} from "../context/AppContext"

function App() {
    const [page, setPage] = useState<PageState>(PageState.MATCHES)

    return <>
        <AppProvider>
            <Toaster richColors position="top-right" />
            <TopBar page={page} setPage={setPage}/>
            {page === PageState.MATCHES && <MatchesCalendar/>}
            {page === PageState.LEADERBOARD && <LeaderBoard/>}
        </AppProvider>
    </>

}

export default App
