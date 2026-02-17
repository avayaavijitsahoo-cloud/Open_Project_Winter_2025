import torch
from torch.utils.data import DataLoader
from data import DensityMatrixDataset
from model import DensityNet


def build_density_matrix(L_flat):
    L = L_flat.view(-1, 4, 4)
    rho = L @ L.transpose(-1, -2)
    rho = rho / torch.trace(rho, dim1=1, dim2=2).view(-1, 1, 1)
    return rho


def train():
    dataset = DensityMatrixDataset(2000)
    loader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = DensityNet()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(50):
        total_loss = 0
        for x, y in loader:
            pred_L = model(x)
            loss = loss_fn(pred_L, y)

            opt.zero_grad()
            loss.backward()
            opt.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

    torch.save(model.state_dict(), "outputs/model.pt")


if __name__ == "__main__":
    train()
