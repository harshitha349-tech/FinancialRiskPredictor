import React from 'react';
export default function RiskBars({dimensions={}}){return <div className="risk-bars">{Object.entries(dimensions).map(([k,v])=><div className="risk-row" key={k}><div><span>{k.replaceAll('_',' ')}</span><b>{v}</b></div><div className="bar"><i style={{width:`${v}%`}}/></div></div>)}</div>}
