import { useContext, useState } from "react"
import "../css/FilterButton.css"
import { AppContext } from "../../context/AppContext"

function FilterButton() {

    const [date, setDate] = useState<string>("")
    const [isOpen, setIsOpen] = useState<boolean>(false)
    const context = useContext(AppContext) 

    function handleFilter(e: React.MouseEvent<HTMLButtonElement>) {
        e.preventDefault();
        e.stopPropagation();
        context.setDateFilter(date || null)
    }

    function handleClick(e: React.MouseEvent<HTMLDivElement>) {
        e.preventDefault();
        setIsOpen(!isOpen);
    }

    return <>
        <div className="filter-container" onClick={handleClick}>
            <img src="../../static/bars-filter.svg" height="25px" width="25px" />
            <div className="filter-input-container" style={{ display: isOpen ? "flex" : "none" }}>
                <input type="date" value={date} onChange={e => setDate(e.target.value)} onClick={(e) => e.stopPropagation()}/>
                <button type="submit" onClick={handleFilter}>Filter</button>
            </div>
        </div>
    </>
}

export default FilterButton
