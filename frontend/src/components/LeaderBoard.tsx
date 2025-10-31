import { useEffect, useState } from "react";
import LeaderBoardCard from "./LeaderBoardCard";
import { SportType } from "../types/sportEnums";
import SportFilter from "./SportFilter";

import "../css/LeaderBoard.css"

function LeaderBoard() {

    const [loading, setLoading] = useState(true)
    const [cards, setCards] = useState<LeaderBoardCardProps[]>([])
    const [sportFilter, setSportFilter] = useState<SportType>(SportType.FOOTBALL)

    useEffect(() => {
        setLoading(true)
        fetch('http://localhost:5000/leaderboard', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                sport: `${sportFilter.toString()}`
            })
        })
            .then(response => response.json())
            .then(data => {
                setCards(data)
                setLoading(false)
            })
            .catch(error => {
                console.error('Request error:', error);
            });
    }, [sportFilter])

    if (loading) {
        return (
            <>
                <SportFilter sportFilter={sportFilter} setSportFilter={setSportFilter} />
                <div className="loading-container">
                    <div className="loading-skeleton"></div>
                </div>
            </>
        )
    } else {
        return <div>
            <SportFilter sportFilter={sportFilter} setSportFilter={setSportFilter} />
            <div className="board-container">
                {cards.map(card => <LeaderBoardCard team_name={card.team_name} location_name={card.location_name} wins={card.wins} key={card.team_name} />)}
            </div>
        </div>
    }

}

export default LeaderBoard
