import "./App.css";
import { collection, getDocs } from "firebase/firestore";
import { useEffect, useState } from "react";
import { db } from "./firebase";

function App() {
  const [votes, setVotes] = useState([]);
  const votesCollectionRef = collection(db, "votes");

  useEffect(() => {
    const getVotes = async () => {
      const data = await getDocs(votesCollectionRef);
      setVotes(data.docs.map((doc) => ({ ...doc.data(), id: doc.id })));
    };
    getVotes();
  }, [votesCollectionRef]);

  return (
    <div className="app">
      <h2>Voting Simulation</h2>
      <div className="Voting-section">Test</div>
      {votes.map((vote) => {
        return <div>{vote.count}</div>;
      })}
    </div>
  );
}

export default App;
