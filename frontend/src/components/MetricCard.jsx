import React from 'react';
export default function MetricCard({label,value,sub,accent}){return <div className="metric-card"><span>{label}</span><strong className={accent||''}>{value}</strong>{sub&&<small>{sub}</small>}</div>}
