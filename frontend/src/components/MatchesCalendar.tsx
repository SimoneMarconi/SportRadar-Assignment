import { useContext, useEffect, useState } from "react";
import PageFilter from "./PageFilter";
import { CardStatus } from "../types/sportEnums";
import SportCard from "./SportCard";
import { AppContext } from "../../context/AppContext";

function MatchesCalendar() {

    // const [loading, setLoading] = useState(true)
    const [pageFilter, setPageFilter] = useState<CardStatus>(CardStatus.LIVE)
    const [cards, setCards] = useState<SportCardProps[]>([])
    const context = useContext(AppContext)

    useEffect(() => {
        setCards(context.cards)
    }, [context.cards])

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
    if (context.loading) {
        return (
            <>
                <PageFilter filter={pageFilter} setFilter={setPageFilter} />
                <div className="loading-container">
                    <div className="loading-skeleton">
                        <div className="loader"></div>
                    </div>
                </div>
            </>
        )
    } else {
        return (
            <>
                <PageFilter filter={pageFilter} setFilter={setPageFilter} />
                <div className="cards-grid">
                    {getDisplayCards().map(card => <SportCard {...card} key={card.match_id} />)}
                </div>
            </>

        )
    }
}

export default MatchesCalendar
