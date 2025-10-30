import ReactDOM from "react-dom"

import "../css/CardOverlay.css"
import { useEffect, useState } from "react";

function CardOverlay(props: OverlayProps) {

    const [cardInfo, setCardInfo] = useState<MatchInfo>({} as MatchInfo)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch("http://localhost:5000/single_match", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ match_id: props.match_id }),
        }).then(
            response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                response.json().then(data => setCardInfo(data[0] as MatchInfo))
                console.log("ciao")
                setLoading(false)
            }
        )
    }, [props.match_id])

    if (!props.isOverlay) return null

    function overlayClick(e: React.MouseEvent) {
        e.preventDefault()
        e.stopPropagation()
        props.setIsOverlay(false)
    }

    const overlay = !loading ? (
        <div className="overlay" onClick={overlayClick} style={{ display: props.isOverlay ? "" : "none" }}>
            <div className="overlay-container">
                <div className="game-description">
                    <p>Description: </p>
                    {cardInfo.match_description === null ? "No description for this match" : cardInfo.match_description}
                </div>
                <div className="team1-description">
                    <p>{cardInfo.team1}:</p>
                    {cardInfo.team1_description === null ? "No description for this match" : cardInfo.team1_description}
                </div>
                <div className="team2-description">
                    <p>{cardInfo.team2}:</p>
                    {cardInfo.team2_description === null ? "No description for this match" : cardInfo.team2_description}
                </div>
                <div className="location-description">
                    <p>Coordinates for the location:</p>
                    {cardInfo.coordinates}
                </div>
                <div className="final-container">
                    <span className="tickets-sold">
                        <p>Total Tickets Sold:</p>
                        {cardInfo.tickets_sold}
                    </span>
                    <span className="total-seats">
                        <p>Total Seats:</p>
                        {cardInfo.total_seats}
                    </span>
                </div>
            </div>
        </div>) : (
        <div className="overlay">
            <div className="overlay-container loading">
                <div className="loader"></div>
            </div>
        </div>)

    return ReactDOM.createPortal(overlay, document.body)
}

export default CardOverlay
