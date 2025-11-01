import { useState } from "react";
import "../css/AddEventOverlay.css";

function AddEventOverlay(props: EventOverlayProps) {

    const [team1, setTeam1] = useState("")
    const [team2, setTeam2] = useState("")
    const [location, setLocation] = useState("")
    const [date, setDate] = useState("")
    const [time, setTime] = useState("")
    const [description, setDescription] = useState("")
    const [ticketsSold, setTicketsSold] = useState<string>("0")

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        fetch("http://localhost:5000/add_match", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                team1,
                team2,
                location,
                date,
                time,
                description,
                tickets_sold: Number(ticketsSold)
            }),
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                props.setIsOpen(false)
            })
            .catch(error => {
                console.error('Request error:', error);
            });
    }

    function handleClose(e: React.MouseEvent) {
        e.stopPropagation()
        props.setIsOpen(false)
    }

    if (!props.isOpen) return null

    return <div className="add-event-overlay" style={{ display: props.isOpen ? "" : "none" }} onClick={handleClose}>
        <form
            className="add-event-form"
            onSubmit={handleSubmit}
        >
            <div>
                <label>Team 1:</label>
                <input
                    type="text"
                    value={team1}
                    onChange={e => setTeam1(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Team 2:</label>
                <input
                    type="text"
                    value={team2}
                    onChange={e => setTeam2(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Location:</label>
                <input
                    type="text"
                    value={location}
                    onChange={e => setLocation(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Date:</label>
                <input
                    type="date"
                    value={date}
                    onChange={e => setDate(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Time:</label>
                <input
                    type="time"
                    value={time}
                    onChange={e => setTime(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Description:</label>
                <textarea
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                    rows={3}
                    placeholder="Brief description of the event"
                />
            </div>
            <div>
                <label>Tickets sold:</label>
                <input
                    type="number"
                    min="0"
                    step="1"
                    value={ticketsSold}
                    onChange={e => setTicketsSold(e.target.value)}
                />
            </div>
            <div>
                <button type="submit">Add Event</button>
                {handleClose &&
                    <button type="button" onClick={handleClose}>Cancel</button>
                }
            </div>
        </form>
    </div>
}

export default AddEventOverlay
