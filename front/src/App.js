import "./App.css";
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
  }, [usersCollectionRef]);

  return (
    <div className="App">
      <h2>Voting Simulation</h2>
      {votes.map((vote) => {
        return <div>{vote}</div>;
      })}
    </div>
  );
}

export default App;
