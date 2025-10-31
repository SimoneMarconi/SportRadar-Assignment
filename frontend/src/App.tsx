import { useState } from 'react'
import './css/App.css'
import { PageState } from './types/sportEnums'
import MatchesCalendar from './components/MatchesCalendar'
import LeaderBoard from './components/LeaderBoard'
import TopBar from './components/TopBar'

function App() {
    const [page, setPage] = useState<PageState>(PageState.MATCHES)

    return <>
        <TopBar page={page} setPage={setPage}/>
        {page === PageState.MATCHES && <MatchesCalendar/>}
        {page === PageState.LEADERBOARD && <LeaderBoard/>}
    </>

}

export default App
