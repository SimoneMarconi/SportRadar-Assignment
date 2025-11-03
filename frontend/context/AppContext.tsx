import React, { createContext, useEffect, useState } from "react";

export const AppContext = createContext<AppContextValue>({} as AppContextValue);

export default function AppProvider(props: { children: React.ReactNode }) {
    const [cards, setCards] = useState<SportCardProps[]>([]);
    const [dateFilter, setDateFilter] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true)

    function fetchAll() {
        fetch("http://localhost:5000/get_all_match")
            .then(response => response.json())
            .then(data => {
                setCards(data as SportCardProps[]);
                setLoading(false)
            })
    }

    useEffect(() => {
        setLoading(true)
        if (!dateFilter) {
            fetchAll();
        } else {
        fetch("http://localhost:5000/match_after", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ time: dateFilter }),
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setCards(data as SportCardProps[]);
                setLoading(false)
            })
        }
    }, [dateFilter]);

    const value: AppContextValue = {
        cards,
        loading,
        setLoading,
        dateFilter,
        setDateFilter,
        refresh: fetchAll,
    };

    return (
        <AppContext.Provider value={value}>
            {props.children}
        </AppContext.Provider>
    );
}
