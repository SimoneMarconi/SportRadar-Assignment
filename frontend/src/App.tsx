import { useState } from 'react'
import './css/App.css'
import TopBar from './components/TopBar'
import { CardStatus } from './types/sportEnums'
import PageFilter from './components/PageFilter'
import SportCard from './components/SportCard'

function App() {

    const [pageFilter, setPageFilter] = useState<CardStatus>(CardStatus.LIVE)
    const dummyCard: SportCardProps = {
        team1: "Milan",
        team2: "Inter",
        location_name: "Stadio Dorico",
        time: "10:00",
        date: "2025-10-20",
        score1: 0,
        score2: 1,
        isLive: true,
        sport: "Football",
        tickets_sold: 1000,
        description: "Il passetto sarà un macello"
    }

    return (
        <>
            <TopBar />
            <PageFilter filter={pageFilter} setFilter={setPageFilter} />
                <SportCard props={dummyCard}/>
        </>
    )
}

export default App
