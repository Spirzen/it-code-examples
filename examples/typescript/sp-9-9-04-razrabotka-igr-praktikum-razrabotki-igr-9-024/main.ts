export function RewardScreen() {
  const { run, dispatch } = useGame();
  return (
    <div className="screen">
      <h2>Награда</h2>
      <p>Золото +{run.combat?.goldReward ?? 0}</p>
      <div className="reward-row">
        {run.rewardCards.map((card, i) => (
          <CardView
            key={i}
            card={card}
            playable
            onClick={() => dispatch({ type: 'PICK_REWARD', index: i })}
          />
        ))}
      </div>
      <button type="button" className="btn" onClick={() => dispatch({ type: 'SKIP_REWARD' })}>
        Пропустить
      </button>
    </div>
  );
}
