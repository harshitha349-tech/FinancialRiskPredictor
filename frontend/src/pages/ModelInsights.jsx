import React from 'react';
import { useEffect, useState } from 'react';
import { api } from '../services/api';
import MetricCard from '../components/MetricCard';
import SectionHeader from '../components/SectionHeader';

export default function ModelInsights() {
  const [m, setM] = useState(null);

  useEffect(() => {
    api.metrics().then(setM).catch(() => {});
  }, []);

  if (!m)
    return <div className="loading">Loading model metrics…</div>;

  const s = m.selected_model;
  const x = m.metrics[s];

  return (
    <>
      <SectionHeader
        title="Model Insights"
        subtitle={`Selected model: ${s}. Metrics are calculated from the held-out test set.`}
      />

      <div className="metrics">
        <MetricCard
          label="Accuracy"
          value={(x.accuracy * 100).toFixed(1) + '%'}
        />

        <MetricCard
          label="Precision"
          value={(x.precision * 100).toFixed(1) + '%'}
        />

        <MetricCard
          label="Recall"
          value={(x.recall * 100).toFixed(1) + '%'}
        />

        <MetricCard
          label="F1-score"
          value={(x.f1 * 100).toFixed(1) + '%'}
        />

        <MetricCard
          label="ROC-AUC"
          value={x.roc_auc.toFixed(3)}
        />
      </div>

      <div className="panel">
        <SectionHeader title="Model Comparison" />

        <table>
          <thead>
            <tr>
              <th>Model</th>
              <th>Accuracy</th>
              <th>Precision</th>
              <th>Recall</th>
              <th>F1</th>
              <th>ROC-AUC</th>
            </tr>
          </thead>

          <tbody>
            {Object.entries(m.metrics).map(([name, v]) => (
              <tr key={name}>
                <td>
                  <b>{name}</b>
                </td>

                <td>{(v.accuracy * 100).toFixed(1)}%</td>
                <td>{(v.precision * 100).toFixed(1)}%</td>
                <td>{(v.recall * 100).toFixed(1)}%</td>
                <td>{(v.f1 * 100).toFixed(1)}%</td>
                <td>{v.roc_auc.toFixed(3)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="grid-2">
        <div className="panel">
          <SectionHeader
            title="Confusion Matrix"
            subtitle="Selected model on the held-out test set"
          />

          <div className="confusion">
            <div></div>

            <b>Predicted Good</b>
            <b>Predicted Bad</b>

            <b>Actual Good</b>

            <strong>{x.confusion_matrix?.[0]?.[0] ?? 0}</strong>
            <strong>{x.confusion_matrix?.[0]?.[1] ?? 0}</strong>

            <b>Actual Bad</b>

            <strong>{x.confusion_matrix?.[1]?.[0] ?? 0}</strong>
            <strong>{x.confusion_matrix?.[1]?.[1] ?? 0}</strong>
          </div>
        </div>

        <div className="panel">
          <SectionHeader
            title="Feature Importance"
            subtitle="Permutation importance using ROC-AUC"
          />

          <div className="distribution">
            {(m.feature_importance || [])
              .slice(0, 8)
              .map((f) => (
                <div key={f.feature}>
                  <div className="dist-top">
                    <span>{f.feature.replaceAll('_', ' ')}</span>
                    <b>{f.importance.toFixed(3)}</b>
                  </div>

                  <div className="bar">
                    <i
                      style={{
                        width: `${Math.min(
                          100,
                          f.importance * 1000
                        )}%`
                      }}
                    />
                  </div>
                </div>
              ))}
          </div>
        </div>
      </div>

      <div className="panel">
        <SectionHeader title="Model Selection" />

        <p>
          CreditLens compares Logistic Regression, Random Forest, and
          Gradient Boosting. The final model is selected using F1-score first
          and ROC-AUC as a tie-breaker so that minority-class detection is
          considered instead of accuracy alone.
        </p>
      </div>
    </>
  );
}