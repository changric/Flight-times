import './App.css';
import Map from './Map.png';
import { Button } from './components/Button';

function App() {
  return (
    <div className="App-header">
      <img src={Map}/>
      <Button location={"Vancouver"}/>
    </div>
  );
}

export default App;
