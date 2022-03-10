import "./App.css";
import { collection, getDocs } from "firebase/firestore";
import { useEffect, useState } from "react";
import { db } from "./firebase";

export default function App() {
  const [allvotes, setAllVotes] = useState([]);
  const votesCollectionRef = collection(db, "test");

  useEffect(() => {
    const getVotes = async () => {
      const data = await getDocs(votesCollectionRef);
      console.log(data);
      setAllVotes(data.docs.map((doc) => ({ ...doc.data(), id: doc.id })));
    };
    getVotes();
  }, []);

  return (
    <div className="App">
      <h2>Voting Simulation</h2>
      <div
        className="Voting-section"
        style={{
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
          padding: "10px",
        }}
      >
        Test
        {allvotes.map((vote) => {
          return <p>{`db: ${vote.name} & ${vote.age}`}</p>;
        })}
      </div>
    </div>
  );
}
