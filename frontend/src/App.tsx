import { useEffect, useState } from 'react'
import './css/App.css'
import TopBar from './components/TopBar'
import { CardStatus } from './types/sportEnums'
import PageFilter from './components/PageFilter'
import SportCard from './components/SportCard'

function App() {
    const [cards, setCards] = useState<SportCardProps[]>([])
    const [pageFilter, setPageFilter] = useState<CardStatus>(CardStatus.LIVE)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch('http://localhost:5000/get_all_match', {
        })
            .then(response => response.json())
            .then(data => {
                setCards(data)
                setLoading(false)
            })
            .catch(error => {
                console.error('Request error:', error);
            });
    }, [])

    function getDisplayCards() {
        const now = new Date()
        switch (pageFilter) {
            case CardStatus.LIVE:
                return cards.filter(card => card.live == true)
            case CardStatus.UPCOMING:
                return cards.filter(card => {
                    const cardDate = new Date(card.date)
                    return now < cardDate
                })
            case CardStatus.FINISHED:
                return cards.filter(card => {
                    const cardDate = new Date(card.date)
                    return now > cardDate && card.live == false
                })
        }
    }

    if (loading) {
        return (
            <>
                <TopBar />
                <PageFilter filter={pageFilter} setFilter={setPageFilter} />
                <div className="loading-container">
                    <div className="loading-skeleton"></div>
                </div>
            </>
        )
    } else {
        return (
            <>
                <TopBar />
                <PageFilter filter={pageFilter} setFilter={setPageFilter} />
                <div className="cards-grid">
                    {getDisplayCards().map(card => <SportCard {...card} key={card.match_id} />)}
                </div>
            </>
        )
    }

}

export default App
