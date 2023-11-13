import { useState } from "react";
import "./index.css"; // Replace 'your-styles.css' with the actual path to your CSS file.
import Controller from "./components/Controller";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <>
        <Controller />
      </>
    </div>
  );
}

export default Controller;
